import json,re,time
from pathlib import Path
from genlayer_py import create_account,create_client
from genlayer_py.chains import studionet
from genlayer_py.contracts import actions as contract_actions

def calldata_compat(method=None,args=None,kwargs=None):
 result={}
 if method is not None: result['method']=method
 if args: result['args']=args
 if kwargs: result['kwargs']=kwargs
 return result
contract_actions.make_calldata_object=calldata_compat
ROOT=Path(__file__).parents[1]; ENV=(ROOT.parents[3]/'accounts.env').read_text(encoding='utf-8')
def key(n): return re.search(r'^ACCOUNT_'+str(n)+r'_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)',ENV,re.M).group(1).strip()
clients={n:create_client(chain=studionet,account=create_account(account_private_key=key(n))) for n in (1,2,3)}; address=json.loads((ROOT/'deployment.json').read_text())['contractAddress']
def finalized(n,name,args,expected='SUCCESS'):
 client=clients[n]; tx=client.write_contract(address=address,function_name=name,args=args); print(name+'_tx='+str(tx),flush=True)
 receipt=client.wait_for_transaction_receipt(transaction_hash=tx,wait_until='finalized',retries=180,interval=5000,full_transaction=True); leader=(receipt.get('consensus_data',{}).get('leader_receipt') or [{}])[0]
 assert receipt.get('result_name')=='MAJORITY_AGREE' and leader.get('execution_result')==expected,receipt
 return str(tx),leader
stamp=str(int(time.time())); board='WHEEL-'+stamp; slots=['Tue 20 Oct 2026 15:00 UTC','Tue 20 Oct 2026 17:00 UTC','Wed 21 Oct 2026 09:00 UTC','Thu 22 Oct 2026 10:00 UTC']
open_tx,_=finalized(2,'open_wheel',[board,'Editorial review', 'UTC',slots,2]); first_tx,_=finalized(1,'cast_availability',[board,'I can join Tuesday at 15:00 UTC or Tuesday at 17:00 UTC.']); before=clients[2].read_contract(address=address,function_name='get_wheel',args=[board]); duplicate_tx,duplicate_leader=finalized(1,'cast_availability',[board,'I changed my mind and want another response.'],expected='ERROR'); unchanged=clients[2].read_contract(address=address,function_name='get_wheel',args=[board]); assert before==unchanged
second_tx,_=finalized(3,'cast_availability',[board,'Tuesday at 17:00 UTC works for me, and Thursday at 10:00 UTC is also possible.']); finalize_tx,_=finalized(2,'finalize_wheel',[board]); final=clients[2].read_contract(address=address,function_name='get_wheel',args=[board]); assert final['state']=='UNANIMOUS' and final['chosen_index']==1,final
proof={'wheelId':board,'transactions':{'openWheel':open_tx,'firstAvailability':first_tx,'duplicateRejected':duplicate_tx,'secondAvailability':second_tx,'finalizeWheel':finalize_tx},'negativeExecution':duplicate_leader.get('execution_result'),'stateUnchangedAfterDuplicate':before==unchanged,'finalWheel':final,'fixtureDisclosure':'The organizer and participants are separately signed operator-controlled technical wallets.'}
(ROOT/'evidence').mkdir(exist_ok=True); (ROOT/'evidence'/'live-run.json').write_text(json.dumps(proof,indent=2)+'\n',encoding='utf-8'); print(json.dumps(proof,indent=2),flush=True)
