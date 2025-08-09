import requests, os, time, webbrowser
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

webbrowser.open("https://t.me/+mQNHQga5lexiNjVi")
console = Console()

def banner():
    console.print(Panel.fit(
        "[bold red]D@rkNet Tools🛠[/bold red] — [bold cyan]OSINT TOOL[/bold cyan]\n[green]Владелец:[/green] [bold yellow]@affteralI | Ghostoraner[/bold yellow]",
        box=box.DOUBLE, padding=(1, 4)))

def get_info(ip):
    r = requests.get(f"http://ipwho.is/{ip}").json()
    return {
        "IP": r.get("ip", "N/A"),
        "Город": r.get("city", "N/A"),
        "Регион": r.get("region", "N/A"),
        "Страна": r.get("country", "N/A"),
        "Провайдер": r.get("connection", {}).get("isp", "N/A"),
        "Континент": r.get("continent", "N/A"),
        "Флаг": r.get("flag", {}).get("emoji", ""),
        "VPN / Proxy": "Да" if r.get("security", {}).get("proxy", False) else "Нет",
        "TOR": "Да" if r.get("security", {}).get("tor", False) else "Нет",
        "Хостинг": "Да" if r.get("security", {}).get("hosting", False) else "Нет",
        "Широта": r.get("latitude", "N/A"),
        "Долгота": r.get("longitude", "N/A"),
    }

def show_info(data):
    table = Table(title="Результат OSINT-анализа", box=box.SQUARE)
    table.add_column("Поле", style="cyan", no_wrap=True)
    table.add_column("Значение", style="magenta")
    for key, value in data.items():
        table.add_row(key, str(value))
    console.print(table)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    console.print("\n[bold green]Введите IP-адрес для анализа:[/bold green] ", end="")
    ip = input().strip()
    console.print("\n[bold blue]🔍 Анализируем...[/bold blue]")
    time.sleep(1)
    info = get_info(ip)
    show_info(info)
    console.print("\n[bold dark_green]Готово. Следи за обновлениями на Telegram-канале![/bold dark_green]")

if __name__ == "__main__":
    main()
