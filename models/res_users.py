# -*- coding: utf-8 -*-
import logging

import werkzeug.urls
import urlparse
import urllib2
import simplejson

import openerp
from openerp.addons.auth_signup.res_users import SignupError
from openerp import models, fields, api
from openerp import SUPERUSER_ID

from openerp.addons.base.res import res_users
res_users.USER_PRIVATE_FIELDS.append('oauth_access_token')
_logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'res.users'

    def _auth_oauth_rpc(self, cr, uid, endpoint, access_token, context=None):
        params = werkzeug.url_encode({'access_token': access_token})#, 'fields': 'name,email,address'})
        _logger.error(params)
        _logger.error(endpoint)
        if urlparse.urlparse(endpoint)[4]:
            url = endpoint + '&' + params
        else:
            url = endpoint + '?'  + params
        _logger.error(url)
        f = urllib2.urlopen(url)
        response = f.read()
        _logger.error(response)

        newResponse = simplejson.loads(response)
        if 'user_id' in newResponse.keys():
            newResponse = newResponse
        elif 'id' in newResponse.keys():
            newResponse['user_id'] = newResponse['id']

        if 'email' in newResponse.keys():
            newResponse['verified_email'] = True

        _logger.error(newResponse)

        return newResponse
