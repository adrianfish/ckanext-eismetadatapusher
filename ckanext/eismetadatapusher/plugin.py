import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import logging
import ckan.logic.action.get as get
import ckan.logic.action.update as update

class EISMetadataPusher(plugins.SingletonPlugin):
    plugins.implements(plugins.IResourceController, inherit=True)

    def after_create(self, context, resource):
        log = logging.getLogger('ckan')
        filename = resource['url']
        last_slash = filename.rfind("/")
        if (last_slash != -1):
            filename = filename[last_slash+1:]
        package = toolkit.get_action('package_show')({}, {'id': resource['package_id']})
        if (package['num_tags'] > 1): 
            tags = package['tags']
            tags.append({'name': 'Eiffel Tower'})
            package['tags'] = tags
        else:
            package['tags'] = [{'name': 'Eiffel Tower'}]
        package = toolkit.get_action('package_update')({}, package)
