from webinar import views
import sys

def test_home_works_correctly(rf, capsys):
    request = rf.get('/chemin/vers/home')
    response = views.home(request)
    print('Tout est ok dans ce test')
    assert response.status_code == 200
        
def test_home_view_cbv_xorks_correctly(rf):
    home_view = views.HomzView.as_view()
    request = rf.post('/chemin/vers/home')
    response = home_view(request)