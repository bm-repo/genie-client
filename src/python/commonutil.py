class CommonUtils:
    def generate_binds_question_mark(self, binds: list) -> str:
        if binds is None:
            raise Exception(
                'binds cannot be null to generate_binds_question_mark')
        return ','.join(['?' for i in range(len(binds))])