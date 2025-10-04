# API Management Service
resource "azurerm_api_management" "main" {
  name                = var.api_management_name
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  publisher_name      = "Know Your Name AI"
  publisher_email     = "admin@knowyourname.com"

  sku_name = "Developer_1"

  tags = var.tags
}

# API Management API
resource "azurerm_api_management_api" "name_analysis" {
  name                = "name-analysis-api"
  resource_group_name = azurerm_resource_group.main.name
  api_management_name = azurerm_api_management.main.name
  revision            = "1"
  display_name        = "Name Analysis API"
  path                = "api"
  protocols           = ["https"]

  service_url = "https://${azurerm_kubernetes_cluster.main.fqdn}/api"

  import {
    content_format = "swagger-json"
    content_value  = jsonencode({
      swagger = "2.0"
      info = {
        title   = "Name Analysis API"
        version = "1.0"
      }
      paths = {
        "/nameanalysis/analyze" = {
          post = {
            summary = "Analyze a name"
            parameters = []
            responses = {
              "200" = {
                description = "Success"
              }
            }
          }
        }
        "/nameanalysis/health" = {
          get = {
            summary = "Health check"
            responses = {
              "200" = {
                description = "Healthy"
              }
            }
          }
        }
      }
    })
  }
}

# API Management Product
resource "azurerm_api_management_product" "name_analysis" {
  product_id            = "name-analysis"
  api_management_name   = azurerm_api_management.main.name
  resource_group_name   = azurerm_resource_group.main.name
  display_name          = "Name Analysis"
  subscription_required = true
  approval_required     = false
  published             = true
}

# Link API to Product
resource "azurerm_api_management_product_api" "name_analysis" {
  api_name            = azurerm_api_management_api.name_analysis.name
  product_id          = azurerm_api_management_product.name_analysis.product_id
  api_management_name = azurerm_api_management.main.name
  resource_group_name = azurerm_resource_group.main.name
}
