# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2022 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
"""This module sets up test environment for aries_alice skill."""

import json
from pathlib import Path
from typing import cast

from aea.helpers.search.models import (
    Attribute,
    Constraint,
    ConstraintType,
    DataModel,
    Description,
    Location,
    Query,
)
from aea.protocols.dialogue.base import DialogueMessage
from aea.test_tools.test_skill import BaseSkillTestCase

from packages.fetchai.protocols.http.message import HttpMessage
from packages.fetchai.protocols.oef_search.message import OefSearchMessage
from packages.fetchai.skills.aries_alice.behaviours import AliceBehaviour
from packages.fetchai.skills.aries_alice.dialogues import (
    DefaultDialogues,
    HttpDialogues,
    OefSearchDialogues,
)
from packages.fetchai.skills.aries_alice.handlers import (
    DefaultHandler,
    HttpHandler,
    OefSearchHandler,
)
from packages.fetchai.skills.aries_alice.strategy import Strategy

from tests.conftest import ROOT_DIR


class AriesAliceTestCase(BaseSkillTestCase):
    """Sets the aries_alice class up for testing."""

    path_to_skill = Path(ROOT_DIR, "packages", "fetchai", "skills", "aries_alice")

    @classmethod
    def setup(cls):
        """Setup the test class."""
        cls.location = {"longitude": 0.1270, "latitude": 51.5194}
        cls.service_data = {"key": "seller_service", "value": "some_value"}
        cls.personality_data = {"piece": "genus", "value": "some_personality"}
        cls.classification = {"piece": "classification", "value": "some_classification"}
        cls.admin_host = "127.0.0.1"
        cls.admin_port = 8067
        config_overrides = {
            "models": {
                "strategy": {
                    "args": {
                        "location": cls.location,
                        "service_data": cls.service_data,
                        "personality_data": cls.personality_data,
                        "classification": cls.classification,
                        "admin_host": cls.admin_host,
                        "admin_port": cls.admin_port,
                    }
                }
            },
        }

        super().setup(config_overrides=config_overrides)

        # behaviours
        cls.alice_behaviour = cast(
            AliceBehaviour, cls._skill.skill_context.behaviours.alice,
        )

        # dialogues
        cls.default_dialogues = cast(
            DefaultDialogues, cls._skill.skill_context.default_dialogues
        )
        cls.http_dialogues = cast(
            HttpDialogues, cls._skill.skill_context.http_dialogues
        )
        cls.oef_search_dialogues = cast(
            OefSearchDialogues, cls._skill.skill_context.oef_search_dialogues
        )

        # handlers
        cls.default_handler = cast(
            DefaultHandler, cls._skill.skill_context.handlers.default
        )
        cls.http_handler = cast(HttpHandler, cls._skill.skill_context.handlers.http)
        cls.oef_search_handler = cast(
            OefSearchHandler, cls._skill.skill_context.handlers.oef_search
        )

        # models
        cls.strategy = cast(Strategy, cls._skill.skill_context.strategy)

        cls.logger = cls._skill.skill_context.logger

        # mocked objects
        cls.mocked_method = "SOME_METHOD"
        cls.mocked_url = "www.some-url.com"
        cls.mocked_version = "some_version"
        cls.mocked_headers = "some_headers"
        cls.body_dict = {"some_key": "some_value"}
        cls.body_str = "some_body"
        cls.mocked_body_bytes = json.dumps(cls.body_str).encode("utf-8")
        cls.mocked_query = Query(
            [Constraint("some_attribute_name", ConstraintType("==", "some_value"))],
            DataModel(
                "some_data_model_name",
                [
                    Attribute(
                        "some_attribute_name",
                        str,
                        False,
                        "Some attribute descriptions.",
                    )
                ],
            ),
        )
        cls.mocked_proposal = Description(
            {
                "contract_address": "some_contract_address",
                "token_id": "123456",
                "trade_nonce": "876438756348568",
                "from_supply": "543",
                "to_supply": "432",
                "value": "67",
            }
        )
        cls.mocked_registration_description = Description({"foo1": 1, "bar1": 2})

        cls.registration_message = OefSearchMessage(
            dialogue_reference=("", ""),
            performative=OefSearchMessage.Performative.REGISTER_SERVICE,
            service_description=cls.mocked_registration_description,
        )
        cls.registration_message.sender = str(cls._skill.skill_context.skill_id)
        cls.registration_message.to = cls._skill.skill_context.search_service_address

        # list of messages
        cls.list_of_http_messages = (
            DialogueMessage(
                HttpMessage.Performative.REQUEST,
                {
                    "method": cls.mocked_method,
                    "url": cls.mocked_url,
                    "headers": cls.mocked_headers,
                    "version": cls.mocked_version,
                    "body": cls.mocked_body_bytes,
                },
                is_incoming=False,
            ),
        )

        cls.register_location_description = Description(
            {"location": Location(51.5194, 0.1270)},
            data_model=DataModel(
                "location_agent", [Attribute("location", Location, True)]
            ),
        )
        cls.list_of_messages_register_location = (
            DialogueMessage(
                OefSearchMessage.Performative.REGISTER_SERVICE,
                {"service_description": cls.register_location_description},
                is_incoming=False,
            ),
        )

        cls.register_service_description = Description(
            {"key": "some_key", "value": "some_value"},
            data_model=DataModel(
                "set_service_key",
                [Attribute("key", str, True), Attribute("value", str, True)],
            ),
        )
        cls.list_of_messages_register_service = (
            DialogueMessage(
                OefSearchMessage.Performative.REGISTER_SERVICE,
                {"service_description": cls.register_service_description},
                is_incoming=False,
            ),
        )

        cls.register_genus_description = Description(
            {"piece": "genus", "value": "some_value"},
            data_model=DataModel(
                "personality_agent",
                [Attribute("piece", str, True), Attribute("value", str, True)],
            ),
        )
        cls.list_of_messages_register_genus = (
            DialogueMessage(
                OefSearchMessage.Performative.REGISTER_SERVICE,
                {"service_description": cls.register_genus_description},
                is_incoming=False,
            ),
        )

        cls.register_classification_description = Description(
            {"piece": "classification", "value": "some_value"},
            data_model=DataModel(
                "personality_agent",
                [Attribute("piece", str, True), Attribute("value", str, True)],
            ),
        )
        cls.list_of_messages_register_classification = (
            DialogueMessage(
                OefSearchMessage.Performative.REGISTER_SERVICE,
                {"service_description": cls.register_classification_description},
                is_incoming=False,
            ),
        )

        cls.register_invalid_description = Description(
            {"piece": "classification", "value": "some_value"},
            data_model=DataModel(
                "some_different_name",
                [Attribute("piece", str, True), Attribute("value", str, True)],
            ),
        )
        cls.list_of_messages_register_invalid = (
            DialogueMessage(
                OefSearchMessage.Performative.REGISTER_SERVICE,
                {"service_description": cls.register_invalid_description},
                is_incoming=False,
            ),
        )
