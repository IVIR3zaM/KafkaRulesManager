from kafka_rules_manager import RuleEngine


def test_no_match_no_change():
    rules = RuleEngine.Rule("lorem"),

    engine = RuleEngine.Engine(rules)

    message = RuleEngine.Message("Some Ipsum", RuleEngine.MessageStatuses.NEW)
    engine.process_message(message)

    assert message.status == RuleEngine.MessageStatuses.NEW
    assert message.should_send_at is None


def test_match_only_status_change():
    rules = RuleEngine.Rule("ipsum"),

    engine = RuleEngine.Engine(rules)

    message = RuleEngine.Message("Some Ipsum", RuleEngine.MessageStatuses.NEW)
    engine.process_message(message)

    assert message.status == RuleEngine.MessageStatuses.READY
    assert message.should_send_at is None


def test_match_second_rule_applies():
    rules = RuleEngine.Rule("lorem"), RuleEngine.Rule("ipsum")

    engine = RuleEngine.Engine(rules)

    message = RuleEngine.Message("Some Ipsum", RuleEngine.MessageStatuses.NEW)
    engine.process_message(message)

    assert message.status == RuleEngine.MessageStatuses.READY
    assert message.should_send_at is None
