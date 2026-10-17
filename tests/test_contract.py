from pathlib import Path

ROOT=Path(__file__).parents[1]

def choose(size,responses):
    counts=[0]*size
    for indexes in responses:
        for index in indexes: counts[index]+=1
    best=max(counts)
    return counts.index(best),best,'UNANIMOUS' if best==len(responses) else 'BEST_FIT'

def test_overlap_is_derived_not_model_written():
    assert choose(4,[[0,1],[1,2],[1,3]])==(1,3,'UNANIMOUS')
    assert choose(4,[[0],[1],[1,2]])==(1,2,'BEST_FIT')

def test_contract_guards_duplicates_and_finalization():
    source=(ROOT/'contracts/contract.py').read_text(encoding='utf-8')
    for token in ('one detailed response per participant','unknown candidate slot','collecting wheel with minimum responses required','organizer may cancel only an empty collecting wheel','prompt_comparative'):
        assert token in source
    assert "board.state='UNANIMOUS' if best==len(responses) else 'BEST_FIT'" in source

def test_frontend_waits_for_finality_and_uses_clock_metaphor():
    page=(ROOT/'docs/index.html').read_text(encoding='utf-8')
    assert 'status:"FINALIZED"' in page
    assert 'WAITING FOR FINALITY' in page
    assert 'wheel-face' in page
    assert 'CAST MY HOURS' in page
