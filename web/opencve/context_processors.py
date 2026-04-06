from urllib.parse import urlencode
import os

def canonical_url_context(request):
    query_params = request.GET.dict()

    allowed_params = (
        # Pagination
        "page",
        "product_page",
        # CVEs listing
        "search",
        "vendor",
        "product",
        "weakness",
        "cvss",
    )

    # Remove empty params, not allowed ones and first pages
    query_params_copy = query_params.copy()
    for key, value in query_params_copy.items():
        if (
            not value
            or (key not in allowed_params)
            or (key == "page" and value == "1")
            or (key == "product_page" and value == "1")
        ):
            query_params.pop(key, None)

    # Sort the query params to only have the same order
    sorted_query_params = dict(sorted(query_params.items()))

    # Build the root path with query params
    base_url = request.build_absolute_uri(request.path)
    if sorted_query_params:
        base_url = f"{base_url}?{urlencode(sorted_query_params)}"

    return {"canonical_url": base_url}

def opencve_version(request):
    """Expose the OpenCVE version to all templates."""
    version_file = os.path.join(
        os.path.dirname(__file__),  # web/opencve/
        "../../VERSION"             # root VERSION file
    )
    try:
        with open(os.path.abspath(version_file)) as f:
            version = f.read().strip()
    except FileNotFoundError:
        version = "unknown"
    return {"OPENCVE_VERSION": version}
