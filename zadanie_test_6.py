import pytest
import zadanie_6 as z6


@pytest.fixture
def project():
    p = z6.Project("TesT_14/users.json")
    p.login("Petr","id003")
    return p

def test_level_access(project):
    assert project.levelAccess == 5

def test_add_user(project):
    assert len(project.users) == 4
    project.addUser("P","id005", 7)
    assert len(project.users) == 5

def test_(project):
    with pytest.raises(z6.LevelException):
        project.addUser("V","id006",2) 


if __name__ == '__main__':
    pytest.main(['-v'])