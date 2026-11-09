from rich.console import Console
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    console = Console(force_terminal=True)

    while True:
        console.print("type 0 to exit, press enter to continue\n", style="red")
        action = input()

        if action == "0":
            break

        console.print("available seasons: [2018-19] to [2025-26]", style="magenta")
        console.print("input season (in the format 20xx-xx): ", style="red")
        season = input()

        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

        console.print("input nationality (in uppercase): ", style="red")
        nationality = input()
        print("\n")

        reader = PlayerReader(url)
        players = reader.get_players()
        stats = PlayerStats(players)
        players = stats.top_by_nationality(nationality)

        if players:
            console.print(f"players from {nationality}:\n", style="magenta")
            for player in players:
                console.print(player, style="cyan")
            print("\n")

        else:
            console.print("no players found. please check the input\n", style="bold red")



main()
