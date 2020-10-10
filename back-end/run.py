from app import create_app

mt = create_app()

mt.run(host='localhost', debug=True)
