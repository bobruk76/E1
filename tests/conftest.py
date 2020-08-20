import pytest

@pytest.fixture(params = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage'])
def word(request):
    return request.param

@pytest.fixture(params = ['l', 'a', 'y', 'i', 'p', 'g', 'x', 'v', 'b', 'e', 't', 'o', 'r', 'c', 'f', 'k', 's', 'n', 'u']
)
def true_letter(request):
    return request.param
