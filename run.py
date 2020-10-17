from app import create_app

mask_detection = create_app()

mask_detection.run(host='localhost', debug=True)