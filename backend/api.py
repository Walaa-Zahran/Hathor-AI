from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
from ai_model import generate_risk_score, mint_reputation_nft

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    html = '''
    <html>
    <head><title>HathorAI Demo</title></head>
    <body>
      <h2>HathorAI Wallet Risk Scoring</h2>
      <form method="POST" action="/ui">
        <label for="wallet">Wallet Address:</label><br>
        <input type="text" id="wallet" name="wallet"><br><br>
        <input type="submit" value="Get Score">
      </form>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/ui', methods=['POST'])
def ui_score():
    wallet = request.form.get("wallet")
    if not wallet:
        return "No wallet provided", 400
    score = generate_risk_score(wallet)
    nft = mint_reputation_nft(wallet, score)
    html = f'''
    <html>
    <head><title>Score Result</title></head>
    <body>
      <h2>Score for Wallet: {wallet}</h2>
      <p><strong>Risk Score:</strong> {score}</p>
      <p><strong>NFT ID:</strong> {nft['token_id']}</p>
      <p><strong>Mint Time:</strong> {nft['minted_at']}</p>
      <a href="/">Back</a>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/score', methods=['POST'])
def get_score():
    data = request.json
    wallet = data.get("wallet")
    if not wallet:
        return jsonify({"error": "No wallet address provided"}), 400

    score = generate_risk_score(wallet)
    nft = mint_reputation_nft(wallet, score)

    return jsonify({
        "wallet": wallet,
        "score": score,
        "nft": nft
    })

@app.route('/telegram/score', methods=['GET'])
def telegram_score():
    wallet = request.args.get("wallet")
    if not wallet:
        return "Missing wallet", 400
    score = generate_risk_score(wallet)
    return f"Wallet: {wallet}\nRisk Score: {score}"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
