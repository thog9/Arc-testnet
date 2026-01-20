# Arc Testnet Scripts 🚀 

This collection of Python scripts empowers you to interact seamlessly with the Arc Testnet, a blockchain test network for decentralized applications. The core script, `main.py`, offers automation and multi-account support for core testnet activities.

🔗 Register: [Arc Testnet](https://faucet.circle.com/)

## ✨ Features Overview

### General Features

- **Multi-Account Support**: Reads private keys from `pvkey.txt` to perform actions across multiple accounts.
- **Colorful CLI**: Uses `colorama` for visually appealing output with colored text and borders.
- **Asynchronous Execution**: Built with `asyncio` for efficient blockchain interactions.
- **Error Handling**: Comprehensive error catching for blockchain transactions and RPC issues.
- **Bilingual Support**: Supports both English and Vietnamese output based on user selection.

### Included Scripts

1. **TouchGM**: Touch GM → CoNFT
2. **Produce**: Produce Contract → CoNFT
3. **Mintpet**: Mint Pet & Open Chest → CoPet
4. **Mintcopass**: Check Score & Mint Badge Arc → CoPass
5. **Conftnft**: Mint NFT Community Member of Arc → CoNFT
6. **Domain**: Mint Domain  → CoNFT
7. **Mintzkcodex**: Mint NFT zkCodex Memorial Collection  → zkCodex
8. **Caset**: Mint NFT Collection  → Caset
9. **Oku**: Mint NFT Collection  → OKUXYZ
10. **Mintaura**: Mint NFT Collection  → MintAura
11. **Alze**: Mint NFT Collection → 0xAlze
12. **Morkie**: Mint NFT Collection  → Morkie
13. **Draze**: Mint NFT Collection  → DrazeLab
14. **Znsdomain**: Mint Domain  → ZNS
15. **Infinitydomain**: Mint Domain  → Infinityname
16. **Superbridge**: Bridge USDC (ARC → Sepolia) → Superbridge
17. **Arcflow**: Mint Genesis Pass NFT → ArcFlow Finance
18. **Wrapsynthra**: Wrap/UnWrap USDC | WUSDC → Synthra
19. **Wraparcflow**: Wrap/UnWrap USDC | WUSDC → ArcFlow Finance
20. **Deploy Token**: Deploy Token smart-contract
21. **Send Token**: Send Token ERC20 random or File (addressERC20.txt)
22. **Nft Collection**: Deploy NFT smart-contract
23. **Send TX**: Send TX random or File (address.txt)

## 🛠️ Prerequisites

Before running the scripts, ensure you have the following installed:

- Python 3.8+
- `pip` (Python package manager)
- **Dependencies**: Install via `pip install -r requirements.txt` (ensure `web3.py`, `colorama`, `asyncio`, `eth-account`, `aiohttp_socks` and `inquirer` are included).
- **pvkey.txt**: Add private keys (one per line) for wallet automation.
- **proxies.txt** (optional): Add proxy addresses for network requests, if needed.

## 📦 Installation

1. **Clone this repository:**
   ```sh
   git clone https://github.com/thog9/Arc-testnet.git
   cd Arc-testnet
   ```
2. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Prepare Input Files:**
   - Open the `pvkey.txt`: Add your private keys (one per line) in the root directory.
   ```sh
   nano pvkey.txt 
   ```
   - Create `address.txt`, `addressERC20.txt`, `contractNFT.txt`, `contractERC20.txt`, or `proxies.txt` for specific operations:
   ```sh
   nano address.txt
   nano addressERC20.txt
   nano contractNFT.txt
   nano contractERC20.txt
   nano proxies.txt
   ```
4. **Run:**
   ```sh
   python main.py
   ```
   - Choose a language (Vietnamese/English).

## 📨 Contact

Connect with us for support or updates:

- **Telegram**: [thog099](https://t.me/thog099)
- **Channel**: [CHANNEL](https://t.me/thogairdrops)
- **Group**: [GROUP CHAT](https://t.me/thogchats)
- **X**: [Thog](https://x.com/thog099) 

----

## ☕ Support Us

Love these scripts? Fuel our work with a coffee!

🔗 BUYMECAFE: [BUY ME CAFE](https://buymecafe.vercel.app/)

🔗 WEBSITE: [BUY SCRIPS](https://thogtoolhub.com/)
