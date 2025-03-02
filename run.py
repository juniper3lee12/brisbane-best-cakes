import os
from BestCakesinBrisbane import create_app

if __name__=='__main__':
    napp=create_app()
    napp.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))