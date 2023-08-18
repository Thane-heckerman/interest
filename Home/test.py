from .views import history
from .models import History
from .middleware import SearchHistory
data = history()
print(data)