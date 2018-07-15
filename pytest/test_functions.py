import functions
import pytest

@pytest.mark.parametrize("test_input1,test_input2,expected_output",
                          [
                             (1,1.5,50),
                             (0,1,100),
                             (2,4,100),
                             (0,0,0),
                             (0,2,200),
                             (-1,-2,-100)
                          ]
                         )

def test_growth(test_input1,test_input2,expected_output):
    value = functions.growth(test_input1,test_input2)
    assert value == expected_output

def test_raises_exception_on_string_arguments():
    with pytest.raises(TypeError):
        functions.growth('str1','str2')
@pytest.mark.parametrize("test_input,expected_output",
                          [
                             (5,1),
                             (12,1),
                             (-2,0),
                             (-8,0)
                          ]
                         )
def test_target(test_input,expected_output):
    target_val = functions.target(test_input)
    assert target_val == expected_output
