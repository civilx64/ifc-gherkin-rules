import os
import ifcopenshell
from behave.model import Scenario
from validation_results import flush_results_to_db, OutcomeSeverity

DEVELOPMENT = os.environ.get('environment', 'development').lower() == 'development'
NO_POSTGRES = os.environ.get('NO_POSTGRES', '1').lower() in {'1', 'true'}

model_cache = {}
def read_model(fn):
    if cached := model_cache.get(fn):
        return cached
    model_cache[fn] = ifcopenshell.open(fn)
    return model_cache[fn]

def before_feature(context, feature):
    # @tfk we have this strange issue between stack frames blending over
    # between features so we need to preserve only the bottom two stack
    # frames when beginning a new feature.
    context._stack = context._stack[-2:]

    #@todo incorporate into gherkin error handling
    # assert protocol.enforce(context, feature), 'failed'

    context.model = read_model(context.config.userdata["input"])
    Scenario.continue_after_failed_step = True
    context.gherkin_outcomes = []

def before_step(context, step):
    context.step = step

def after_feature(context, feature):
    execution_mode = context.config.userdata.get('execution_mode')
    if execution_mode and execution_mode == 'ExecutionMode.PRODUCTION':
        flush_results_to_db(context.gherkin_outcomes)
    else: # invoked via console
        pass