import discord, os, sys, colorama, random
from colorama import Fore
client = discord.Client()

r = Fore.RESET
g = Fore.GREEN
R = Fore.RED
colorama.init()
def clear():
    os.system('cls')

os.system(f'title MassDm - V1')
def anal():
    try:
        text = f"""   

			 ♥♥♥♥♥♥  ♥♥♥    ♥♥ ♥♥      ♥♥♥♥♥♥ ♥♥   ♥♥  ♥♥♥♥♥  ♥♥♥    ♥♥ 
			♥♥    ♥♥ ♥♥♥♥   ♥♥ ♥♥     ♥♥      ♥♥   ♥♥ ♥♥   ♥♥ ♥♥♥♥   ♥♥ 
			♥♥    ♥♥ ♥♥ ♥♥  ♥♥ ♥♥     ♥♥      ♥♥♥♥♥♥♥ ♥♥♥♥♥♥♥ ♥♥ ♥♥  ♥♥ 
			♥♥    ♥♥ ♥♥  ♥♥ ♥♥ ♥♥     ♥♥      ♥♥   ♥♥ ♥♥   ♥♥ ♥♥  ♥♥ ♥♥ 
			 ♥♥♥♥♥♥  ♥♥   ♥♥♥♥ ♥♥      ♥♥♥♥♥♥ ♥♥   ♥♥ ♥♥   ♥♥ ♥♥   ♥♥♥♥ 
                                                                 @urmom
        """
        bad_colors = ['LIGHTRED_EX', 'RED']
        codes = vars(colorama.Fore)
        colors = [codes[color] for color in codes if color in bad_colors]
        colored_chars = [random.choice(colors) + char for char in text]
        print(''.join(colored_chars))
       

    except KeyboardInterrupt:
        sys.exit()

@client.event
async def on_ready():
    os.system(f'title MassDm - Authorized: [{client.user.name}#{client.user.discriminator}]')
    anal()
    cmd = input(f"Message Here:{r} ")
    clear()
    anal()
    count = 0
    for user in client.user.friends:
        try:
            count += 1
            await user.send(cmd)
            print(f"{r}[{g}STATUS{r}] [{R}{user.name}{r}] │ {g}Recieved{r}")
            os.system(f'title MassDm - Sent: [{count}] Dm │ User: [{user.name}] │ ID: [{user.id}]')
        except:
            print(f"{r}[{R}STATUS{r}] [{R}{user.name}{r}] | {R}Failed{r}")
client.run("ur shitty token", bot=False)