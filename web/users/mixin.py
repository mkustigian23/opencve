from allauth.socialaccount.adapter import get_adapter


class SocialProvidersMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        providers = get_adapter().list_providers(self.request)
        context["social_providers"] = [
            p
            for p in providers
            if (not p.uses_apps or not p.app.settings.get("hidden"))
        ]

        return context
