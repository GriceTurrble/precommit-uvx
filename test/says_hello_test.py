from python_project_template import main


def test_it_says_hello(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello world!" in captured.out
