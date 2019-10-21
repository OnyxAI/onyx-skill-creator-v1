from os.path import dirname, join

from boilerplate_skill.index import boilerplate
from onyx.skills.core import OnyxSkill
from onyx.util.log import getLogger

__author__ = ''

LOGGER = getLogger(__name__)

class BoilerplateSkill(OnyxSkill):
    def __init__(self):
        super(BoilerplateSkill, self).__init__(name="BoilerplateSkill")

    def get_blueprint(self):
        return boilerplate

    def initialize(self):
        LOGGER.info("Boilerplate Skill initialize")

    def stop(self):
        pass

def create_skill():
    return BoilerplateSkill()
