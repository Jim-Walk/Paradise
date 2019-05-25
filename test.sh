ulimit -s unlimited
cd poem
pytest
cd ../bots
pytest --fulltrace
