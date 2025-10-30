# Excel-to-INI Routing Web App

Upload an Excel routing table (RouteTable sheet) and instantly download a MsgRouterInfo.ini with valid CAN bus logic.

## How to run locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run app:
   ```bash
   python app.py
   ```
3. Visit [http://localhost:10000](http://localhost:10000) in your browser.

## How to deploy on Render.com
1. Push your code (including this file, app.py, requirements.txt) to your GitHub repository.

2. Go to [https://dashboard.render.com/](https://dashboard.render.com/).
3. Click `New +` > `Web Service` and connect your repo.
4. Set:
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: Free
5. Click Create Web Service. Deploy.

6. When ready, visit your Render.com public URL and use your app!

## Troubleshooting
- App failed to build? Make sure `requirements.txt` includes all dependencies and your Flask file is called `app.py` with a variable `app`.
- App not found? Flask app variable must be `app = Flask(__name__)`.
- Excel processing errors? Check your sheet/tab is named exactly `RouteTable`.

## Advanced
- To update: git push changes to your GitHub repository, Render rebuilds automatically.
