import os
import sys
import asyncio
from colorama import init, Fore, Style
import inquirer

# Khởi tạo colorama
init(autoreset=True)

# Độ rộng viền cố định
BORDER_WIDTH = 80

# Hàm hiển thị viền đẹp mắt
def print_border(text: str, color=Fore.CYAN, width=BORDER_WIDTH):
    text = text.strip()
    if len(text) > width - 4:
        text = text[:width - 7] + "..."  # Cắt dài và thêm "..."
    padded_text = f" {text} ".center(width - 2)
    print(f"{color}┌{'─' * (width - 2)}┐{Style.RESET_ALL}")
    print(f"{color}│{padded_text}│{Style.RESET_ALL}")
    print(f"{color}└{'─' * (width - 2)}┘{Style.RESET_ALL}")

# Hàm hiển thị banner
def _banner():
    banner = r"""


░█████╗░██████╗░░█████╗░  ████████╗███████╗░██████╗████████╗███╗░░██╗███████╗████████╗
██╔══██╗██╔══██╗██╔══██╗  ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝████╗░██║██╔════╝╚══██╔══╝
███████║██████╔╝██║░░╚═╝  ░░░██║░░░█████╗░░╚█████╗░░░░██║░░░██╔██╗██║█████╗░░░░░██║░░░
██╔══██║██╔══██╗██║░░██╗  ░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░██║╚████║██╔══╝░░░░░██║░░░
██║░░██║██║░░██║╚█████╔╝  ░░░██║░░░███████╗██████╔╝░░░██║░░░██║░╚███║███████╗░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░  ░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚══╝╚══════╝░░░╚═╝░░░


    """
    print(f"{Fore.GREEN}{banner:^80}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
    print_border("ARC TESTNET", Fore.GREEN)
    print(f"{Fore.YELLOW}│ {'Liên hệ / Contact'}: {Fore.CYAN}https://t.me/thog099{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}│ {'Discord'}: {Fore.CYAN}https://discord.gg/MnmYBKfHQf{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}│ {'Channel Telegram'}: {Fore.CYAN}https://t.me/thogairdrops{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")

# Hàm xóa màn hình
def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')

async def run_touchgm(language: str):
    from scripts.touchgm import run_touchgm as touchgm_run
    await touchgm_run(language)

async def run_sendtx(language: str):
    from scripts.sendtx import run_sendtx as sendtx_run
    await sendtx_run(language)

async def run_deploytoken(language: str):
    from scripts.deploytoken import run_deploytoken as deploytoken_run
    await deploytoken_run(language)

async def run_sendtoken(language: str):
    from scripts.sendtoken import run_sendtoken as sendtoken_run
    await sendtoken_run(language)

async def run_nftcollection(language: str):
    from scripts.nftcollection import run_nftcollection as nftcollection_run
    await nftcollection_run(language)

async def run_produce(language: str):
    from scripts.produce import run_produce as produce_run
    await produce_run(language)

async def run_mintpet(language: str):
    from scripts.mintpet import run_mintpet as mintpet_run
    await mintpet_run(language)

async def run_mintcopass(language: str):
    from scripts.mintcopass import run_mintcopass as mintcopass_run
    await mintcopass_run(language)

async def run_conftnft(language: str):
    from scripts.conftnft import run_conftnft as conftnft_run
    await conftnft_run(language)

async def run_domain(language: str):
    from scripts.domain import run_domain as domain_run
    await domain_run(language)

async def run_mintzkcodex(language: str):
    from scripts.mintzkcodex import run_mintzkcodex as mintzkcodex_run
    await mintzkcodex_run(language)
    
async def cmd_exit(language: str):
    print_border(f"Exiting...", Fore.GREEN)
    sys.exit(0)

# Danh sách lệnh menu
SCRIPT_MAP = {
    "touchgm": run_touchgm,
    "sendtx": run_sendtx,
    "deploytoken": run_deploytoken,
    "sendtoken": run_sendtoken,
    "nftcollection": run_nftcollection,
    "produce": run_produce,
    "mintpet": run_mintpet,
    "mintcopass": run_mintcopass,
    "conftnft": run_conftnft,
    "domain": run_domain,
    "mintzkcodex": run_mintzkcodex,
    "exit": cmd_exit
}

def get_available_scripts(language):
    scripts = {
        'vi': [
            {"name": "1. Touch GM → CoNFT", "value": "touchgm", "locked": True},
            {"name": "2. Produce Contract → CoNFT", "value": "produce", "locked": True},
            {"name": "3. Mint Pet & Open Chest → CoPet", "value": "mintpet", "locked": True},
            {"name": "4. Kiểm tra điểm & Mint Badge Arc → CoPass", "value": "mintcopass", "locked": True},
            {"name": "5. Mint NFT Community Member of Arc → CoNFT", "value": "conftnft", "locked": True},
            {"name": "6. Mint Domain  → CoNFT", "value": "domain", "locked": True},
            {"name": "7. Mint NFT zkCodex Memorial Collection  → zkCodex", "value": "mintzkcodex", "locked": True},
            
            #{"name": "8. ", "value": "", "locked": True},


            {"name": "9. Deploy NFT - Quản lý bộ sưu tập NFT [ Tạo | Mint | Đốt ]", "value": "nftcollection"},
            {"name": "10. Send TX ngẫu nhiên hoặc File (address.txt)", "value": "sendtx"},
            {"name": "11. Deploy Token smart-contract", "value": "deploytoken"},
            {"name": "12. Send Token ERC20 ngẫu nhiên hoặc File (addressERC20.txt)", "value": "sendtoken"},

            {"name": "X. Exit", "value": "exit"},
            
        ],
        'en': [
            {"name": "1. Touch GM → CoNFT", "value": "touchgm", "locked": True},
            {"name": "2. Produce Contract → CoNFT ", "value": "produce", "locked": True},
            {"name": "3. Mint Pet & Open Chest → CoPet", "value": "mintpet", "locked": True},
            {"name": "4. Check Score & Mint Badge Arc → CoPass", "value": "mintcopass", "locked": True},
            {"name": "5. Mint NFT Community Member of Arc → CoNFT", "value": "conftnft", "locked": True},
            {"name": "6. Mint Domain  → CoNFT", "value": "domain", "locked": True},
            {"name": "7. Mint NFT zkCodex Memorial Collection  → zkCodex", "value": "mintzkcodex", "locked": True},
            
            #{"name": "8. ", "value": ""},

            {"name": "9. Deploy NFT - Manage NFT Collection [ Create | Mint | Burn ]", "value": "nftcollection"},
            {"name": "10. Send Random TX or File (address.txt)", "value": "sendtx"},
            {"name": "11. Deploy Token smart-contract", "value": "deploytoken"},
            {"name": "12. Send Token ERC20 Random or File (addressERC20.txt)", "value": "sendtoken"},

            {"name": "X. Exit", "value": "exit"},
        ]
    }
    return scripts[language]

def run_script(script_func, language):
    """Chạy script bất kể nó là async hay không."""
    if asyncio.iscoroutinefunction(script_func):
        asyncio.run(script_func(language))
    else:
        script_func(language)

def select_language():
    while True:
        _clear()
        _banner()
        print(f"{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
        print_border("CHỌN NGÔN NGỮ / SELECT LANGUAGE", Fore.YELLOW)
        questions = [
            inquirer.List('language',
                          message=f"{Fore.CYAN}Vui lòng chọn / Please select:{Style.RESET_ALL}",
                          choices=[("1. Tiếng Việt", 'vi'), ("2. English", 'en')],
                          carousel=True)
        ]
        answer = inquirer.prompt(questions)
        if answer and answer['language'] in ['vi', 'en']:
            return answer['language']
        print(f"{Fore.RED}❌ {'Lựa chọn không hợp lệ / Invalid choice':^76}{Style.RESET_ALL}")

def main():
    _clear()
    _banner()
    language = select_language()

    messages = {
        "vi": {
            "running": "Đang thực thi: {}",
            "completed": "Đã hoàn thành: {}",
            "error": "Lỗi: {}",
            "press_enter": "Nhấn Enter để tiếp tục...",
            "menu_title": "MENU CHÍNH",
            "select_script": "Chọn script để chạy",
            "locked": "🔒 Script này bị khóa! Vui lòng vào group hoặc Role Discord [ OG - Donate ] để mở khóa."
        },
        "en": {
            "running": "Running: {}",
            "completed": "Completed: {}",
            "error": "Error: {}",
            "press_enter": "Press Enter to continue...",
            "menu_title": "MAIN MENU",
            "select_script": "Select script to run",
            "locked": "🔒 This script is locked! Please join the discord group or role [ OG - Donate ] to unlock."
        }
    }

    while True:
        _clear()
        _banner()
        print(f"{Fore.YELLOW}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
        print_border(messages[language]["menu_title"], Fore.YELLOW)
        print(f"{Fore.CYAN}│ {messages[language]['select_script'].center(BORDER_WIDTH - 4)} │{Style.RESET_ALL}")

        available_scripts = get_available_scripts(language)
        questions = [
            inquirer.List('script',
                          message=f"{Fore.CYAN}{messages[language]['select_script']}{Style.RESET_ALL}",
                          choices=[script["name"] for script in available_scripts],
                          carousel=True)
        ]
        answers = inquirer.prompt(questions)
        if not answers:
            continue

        selected_script_name = answers['script']
        selected_script = next(script for script in available_scripts if script["name"] == selected_script_name)
        selected_script_value = selected_script["value"]

        if selected_script.get("locked"):
            _clear()
            _banner()
            print_border("SCRIPT BỊ KHÓA / LOCKED", Fore.RED)
            print(f"{Fore.YELLOW}{messages[language]['locked']}")
            print('')
            print(f"{Fore.CYAN}→ Telegram: https://t.me/thogairdrops")
            print(f"{Fore.CYAN}→ Donate: https://buymecafe.vercel.app{Style.RESET_ALL}")
            print('')
            input(f"{Fore.YELLOW}⏎ {messages[language]['press_enter']}{Style.RESET_ALL:^76}")
            continue

        script_func = SCRIPT_MAP.get(selected_script_value)
        if script_func is None:
            print(f"{Fore.RED}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
            print_border(f"{'Chưa triển khai / Not implemented'}: {selected_script_name}", Fore.RED)
            input(f"{Fore.YELLOW}⏎ {messages[language]['press_enter']}{Style.RESET_ALL:^76}")
            continue

        try:
            print(f"{Fore.CYAN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
            print_border(messages[language]["running"].format(selected_script_name), Fore.CYAN)
            run_script(script_func, language)
            print(f"{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
            print_border(messages[language]["completed"].format(selected_script_name), Fore.GREEN)
            input(f"{Fore.YELLOW}⏎ {messages[language]['press_enter']}{Style.RESET_ALL:^76}")
        except Exception as e:
            print(f"{Fore.RED}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
            print_border(messages[language]["error"].format(str(e)), Fore.RED)
            print('')
            input(f"{Fore.YELLOW}⏎ {messages[language]['press_enter']}{Style.RESET_ALL:^76}")

if __name__ == "__main__":
    main()

