import click

class AIUS:
    def __init__(self):
        self.run_console()

    @click.group()
    @click.pass_context
    @click.option("-h", "--help", is_flag=True, help="Show this message and exit")
    @click.option("-i", "--interactive", is_flag=True, help="Run interactive shell")
    @click.option("-s", "--shell", is_flag=True, help="Run interactive shell. Same as --interactive")
    def run_console(ctx, help, interactive, shell):
        """AIUS CLI - Artificial Intelligence User Shell
        """
        # click.echo(click.style(f'Executing command', fg='green'))
        pass

    @run_console.group("agents")
    def agents():
        """Agent-related commands"""
        pass
    @agents.command()
    def list():
        """List all agents"""
        click.echo("List of all agents")
    @agents.command()
    def create():
        """Create agents"""
        click.echo("Dry run create agents")
    @agents.command()
    def sleep():
        """Sleep agents by ids"""
        click.echo("Dry run sleep agents")
    @agents.command()
    def wake():
        """Wake agents by ids"""
        click.echo("Dry run wake agents")
    @agents.command()
    def kill():
        """Kill agents by ids"""
        click.echo("Dry run kill agents")

    @run_console.group("sensors")
    def input_sensors():
        """Input_sensors commands"""
        pass
    @input_sensors.command()
    def list():
        """List all input_sensors"""
        click.echo("List of all input_sensors")
    @input_sensors.command()
    def create():
        """Create input_sensors"""
        click.echo("Dry run create input_sensors")
    @input_sensors.command()
    def sleep():
        """Sleep a given agent by agent_id"""
        click.echo("Dry run sleep agent")
    @input_sensors.command()
    def wake():
        """Wake a given agent by agent_id"""
        click.echo("Dry run wake agent")
    @input_sensors.command()
    def kill():
        """Kill a given agent by agent_id"""
        click.echo("Dry run killed agent")

    @run_console.group("memory")
    def log_memory():
        """Log_memory commands"""
        pass

    @run_console.group("processing")
    def log_processing():
        """Log_processing commands"""
        pass

    @run_console.group("tools")
    def output_tools():
        """Output_tools commands"""
        pass

