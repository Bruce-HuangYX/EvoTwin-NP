# Typer CLI (placeholder)
import typer

app = typer.Typer(help="EvoTwin-NP CLI")

@app.command()
def train(config: str):
    """Run baseline training with a config file."""
    typer.echo(f"[train] Using config: {config}")

@app.command("eval-np")
def eval_np(config: str):
    """Evaluate NP metrics and plot reliability."""
    typer.echo(f"[eval-np] Using config: {config}")

@app.command()
def evo(config: str):
    """Evolutionary search (CMA-ES/NSGA-II)."""
    typer.echo(f"[evo] Using config: {config}")

def main():
    app()

if __name__ == "__main__":
    main()
