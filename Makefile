.PHONY: help

test:
	[ -z $(migration) ] && echo "No migration name specified" || echo $(migration)

migration:
	[ -z $(migration) ] && echo "\033[1;91mNo migration name specified\033[m" \
	|| python3 database/migrations/make_migration.py $(migration)
