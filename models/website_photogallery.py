from openerp.osv import osv, fields
import base64

class photogallery(osv.Model):

        _name = "website.photogallery"

        def get_image(self, cr, uid, id):
                each = self.read(cr, uid, id, ['image'])
                img = each['image']
                return img

        def _get_image(self, cr, uid, ids, field_name, arg, context={}):
                res = {}
                for each in ids:
                        res[each] = self.get_image(cr, uid, each)
                return res

        _columns = {
        'name': fields.char('Image Title', size=100, required=True),
        'image': fields.binary('Image', filters='*.png,*.jpg,*.gif'),
        'preview': fields.function(_get_image, type="binary", method=True),
        'comments': fields.text('Comments'),
        }

