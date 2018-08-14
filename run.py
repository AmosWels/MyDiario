# from api.models.models import DiaryDatabase
from api.App.views import app

if __name__ == '__main__':
    # DiaryDatabase()
    app.run(debug=True)