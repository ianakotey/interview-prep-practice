from pathlib import Path


class Solution:
    def simplifyPath(self, path: Path | str) -> str:

        valid_chunks: list[str] = []

        for chunk in str(path).split("/"):

            match chunk:

                case "" | ".":  # multiple / (eg. ////... ) or cwd
                    pass
                case "..":
                    try:
                        valid_chunks.pop()  # go
                    except IndexError:
                        pass  # /../../.. is valid

                case _:
                    valid_chunks.append(chunk)

        return "/" + "/".join(valid_chunks)


def test():

    test_runner = Solution()

    test_path_str = "///tmp/../tmp/./././test.txt"
    test_path = Path(test_path_str)

    assert (
        test_runner.simplifyPath(test_path)
        == test_runner.simplifyPath(test_path_str)
        == "/tmp/test.txt"
    )


test()
