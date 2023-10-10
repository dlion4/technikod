class ProfileDashboardMixins:
    model=None

    def _posts(self):
        return (
            self.model.objects.filter(writer=self._user().user_profile)
            .all()
            .order_by("-createdAt")
        )
    def get_context_data(self, **kwargs):
        context = {}
        context['posts'] = self._posts()
        return context
    