from flask import Blueprint, request, jsonify, current_app
from controllers.homepage_controller import HomepageController
from flask_cors import cross_origin

homepage_bp = Blueprint('homepage', __name__)

@homepage_bp.route('/products', methods=['GET', 'OPTIONS'])
@homepage_bp.route('/products/', methods=['GET', 'OPTIONS'])
@cross_origin()
def get_homepage_products():
    """
    Get products from categories selected for homepage display
    ---
    tags:
      - Homepage
    responses:
      200:
        description: List of featured products retrieved successfully
        schema:
          type: array
          items:
            type: object
            properties:
              product_id:
                type: integer
              product_name:
                type: string
              sku:
                type: string
              cost_price:
                type: number
                format: float
              selling_price:
                type: number
                format: float
              media:
                type: array
                items:
                  type: object
                  properties:
                    url:
                      type: string
                    type:
                      type: string
              brand:
                type: object
                properties:
                  brand_id:
                    type: integer
                  name:
                    type: string
              category:
                type: object
                properties:
                  category_id:
                    type: integer
                  name:
                    type: string
      500:
        description: Internal server error
    """
    return HomepageController.get_homepage_products()

@homepage_bp.route('/carousels', methods=['GET', 'OPTIONS'])
@homepage_bp.route('/carousels/', methods=['GET', 'OPTIONS'])
@cross_origin()
def get_homepage_carousels():
    """
    Get all active carousel items for homepage (optionally filter by type).
    Query params:
      - type: 'brand' or 'product' (optional)
    """
    if request.method == 'OPTIONS':
        return '', 200
    try:
        carousel_type = request.args.get('type')
        items = HomepageController.get_homepage_carousels(carousel_type)
        return jsonify(items), 200
    except Exception as e:
        current_app.logger.error(f"Error fetching homepage carousels: {e}")
        return jsonify({'message': 'Failed to fetch homepage carousels.'}), 500 
    