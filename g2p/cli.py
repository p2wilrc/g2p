import click
import yaml
from flask.cli import FlaskGroup
from collections import OrderedDict
from g2p.mappings.langs import cache_langs, LANGS_NETWORK
from g2p.mappings.create_ipa_mapping import create_mapping
from g2p.mappings.utils import is_ipa, is_xsampa
from g2p.mappings import Mapping
from g2p._version import VERSION
from g2p import APP, SOCKETIO, make_g2p


def create_app():
    return APP


@click.version_option(version=VERSION, prog_name="g2p")
@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    '''Management script for G2P'''


@click.argument('in_lang', type=click.Choice([x for x in LANGS_NETWORK.nodes if not is_ipa(x) and not is_xsampa(x)]))
@cli.command()
def generate_ipa_mapping(in_lang):
    ''' Generate English mapping
    '''
    eng_ipa = Mapping(in_lang='eng-ipa', out_lang='eng-arpabet')
    new_mapping = Mapping(in_lang=in_lang, out_lang=f'{in_lang}-ipa')
    click.echo(f"Writing English IPA mapping for {in_lang} to file")
    create_mapping(new_mapping, eng_ipa, write_to_file=True)


@click.argument('out_lang', type=click.Choice(LANGS_NETWORK.nodes))
@click.argument('in_lang', type=click.Choice(LANGS_NETWORK.nodes))
@click.argument('input_text', type=click.STRING)
@cli.command()
def convert(in_lang, out_lang, input_text):
    ''' Convert any text
    '''
    transducer = make_g2p(in_lang, out_lang)
    click.echo(transducer(input_text))


@cli.command()
def update():
    ''' Update cached language files
    '''
    cache_langs()