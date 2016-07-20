from openerp import http

# Route photos from database to website frontend
class website_gallery(http.Controller):
        @http.route(['/page/website.photogallery', '/page/photogallery'], type='http', auth="public", website=True)
        def rooms(self, **kw):
                Photos = http.request.env['website.photogallery']
                return http.request.render("website.photogallery", {'photos': Photos.search([]) })

