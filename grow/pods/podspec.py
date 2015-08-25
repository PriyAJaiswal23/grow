# TODO(jeremydw): Implement.
from grow.pods import locales


class Podspec(object):

  def __init__(self, yaml):
    self.yaml = yaml
    self.flags = yaml.get('flags', {})
    self.grow_version = yaml.get('grow_version')
    self.root_path = self.flags.get('root_path', '').lstrip('/').rstrip('/')
    _default_locale = yaml.get('localization', {}).get('default_locale', None)
    self.default_locale = locales.Locale.parse(_default_locale)
    self.fields = yaml

  def get_config(self):
    return self.yaml

  def __getattr__(self, name):
    if name in self.fields:
      return self.fields[name]
    if '{}@'.format(name) in self.fields:
      return self.fields['{}@'.format(name)]
    return object.__getattribute__(self, name)

  @property
  def root(self):
    return self.fields.get('root')
