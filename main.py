#!/usr/bin/env python3
import sys
from rich import print

sam_file = sys.argv[1]

total = 0
mapq60 = 0

with open(sam_file) as f:
    for line in f:
        if line.startswith("@"):
            continue

        fields = line.split("\t")
        mapq = int(fields[4])

        total += 1
        if mapq == 60:
            mapq60 += 1

percentage = (mapq60 / total * 100) if total > 0 else 0

print(f"Total de lecturas alineadas: [bold magenta]{total}[/bold magenta]")
print(f"Lecturas con valor MAPQ60: [bold red]{mapq60}[/bold red]")
print(f"Porcentaje: [bold blue]{round(percentage, 2)}[/bold blue]")
