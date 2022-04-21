import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class DownloadCsvButtonPlugin(plugins.SingletonPlugin):
    '''Adds a button to download all data as a csv
    '''
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
            'download_csv_button')
