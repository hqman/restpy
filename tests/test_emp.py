import pytest

from orders.models.employee import Employee


@pytest.fixture(scope='module')
def modfix():
    print('module init ...')
    yield Employee('shiwei', 'wang', 111)
    print('module end...')


# test setup
@pytest.fixture
def employee():
    print('setup ....')
    yield Employee('kai', 'wang', 111)

    print('tear down .....')

# test down with pytest
def test_email(employee):
    assert employee.email == 'kai.wang@mei.com'

def test_fullname(employee):
    assert employee.fullname == 'kai wang'

def test_email2(modfix):
    assert modfix.email == 'shiwei.wang@mei.com'

def test_fullname2(modfix):
    assert modfix.fullname == 'shiwei wang'

