from BestCakesinBrisbane import create_app

if __name__=='__main__':
    napp=create_app()
    napp.run(host='0.0.0.0', port=5000)