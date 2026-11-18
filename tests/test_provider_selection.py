import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock

from wardogs.model import ContextModel, provider_chain


class ProviderSelectionTests(unittest.IsolatedAsyncioTestCase):
    async def test_blank_provider_uses_active_astrbot_provider(self):
        context = SimpleNamespace(
            get_current_chat_provider_id=AsyncMock(return_value="local-provider"),
            llm_generate=AsyncMock(return_value=SimpleNamespace(completion_text='{"ok":true}')),
        )
        model = ContextModel(context, "fixture-conversation")
        self.assertEqual(provider_chain(model, vision=True), [""])
        self.assertEqual(await model.generate("fixture", "fixture"), {"ok": True})
        self.assertEqual(context.llm_generate.await_args.kwargs["chat_provider_id"], "local-provider")
