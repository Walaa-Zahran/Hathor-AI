import random
from datetime import datetime

def generate_risk_score(wallet_address: str) -> int:
    """Generate a pseudo AI-based risk score."""
    random.seed(hash(wallet_address))
    return random.randint(30, 95)

def mint_reputation_nft(wallet_address: str, score: int) -> dict:
    """Simulate NFT minting for user reputation."""
    return {
        "token_id": f"nft_{wallet_address[-6:]}_{score}",
        "minted_at": datetime.utcnow().isoformat() + "Z",
        "metadata": {
            "wallet": wallet_address,
            "score": score,
            "type": "Reputation NFT"
        }
    }
