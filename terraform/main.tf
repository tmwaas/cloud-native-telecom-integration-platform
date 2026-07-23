terraform {
  required_version = ">= 1.3.0"
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.20.0"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace" "telecom_platform" {
  metadata {
    name = "telecom-integration-v2"
    labels = {
      environment = "production"
      domain      = "telecom-oss"
    }
  }
}
