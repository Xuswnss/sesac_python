import random
import string
import bcrypt

class PasswordGenerator:
    def __init__(self):
        # 자주 사용되는 비밀번호 패턴들
        self.common_passwords = [
            'password123', 'admin1234', 'qwerty123', 'welcome123',
            'letmein123', 'password1', 'admin123', 'user1234',
            'test1234', 'hello123', 'world123', 'pass123'
        ]
        
        # 비밀번호 구성 요소
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special_chars = '!@#$%^&*'
    
    def generate_random_password(self, length=12):
        """랜덤 비밀번호 생성"""
        # 각 문자 유형에서 최소 1개씩 포함
        password = [
            random.choice(self.lowercase),
            random.choice(self.uppercase),
            random.choice(self.digits),
            random.choice(self.special_chars)
        ]
        
        # 나머지 길이만큼 랜덤하게 채우기
        all_chars = self.lowercase + self.uppercase + self.digits + self.special_chars
        for _ in range(length - 4):
            password.append(random.choice(all_chars))
        
        # 순서 섞기
        random.shuffle(password)
        return ''.join(password)
    
    def generate_pattern_password(self):
        """패턴 기반 비밀번호 생성"""
        patterns = [
            lambda: f"{random.choice(['user', 'admin', 'test'])}{random.randint(100, 9999)}",
            lambda: f"{random.choice(['pass', 'pwd', 'key'])}{random.randint(10, 999)}!",
            lambda: f"{random.choice(['hello', 'world', 'welcome'])}{random.randint(1, 999)}#",
            lambda: f"MyPass{random.randint(10, 99)}@"
        ]
        return random.choice(patterns)()
    
    def generate_password(self):
        """비밀번호 생성 (다양한 패턴 혼합)"""
        password_type = random.choices(
            ['common', 'pattern', 'random'],
            weights=[0.3, 0.4, 0.3],  # 30% 자주사용, 40% 패턴, 30% 랜덤
            k=1
        )[0]
        
        if password_type == 'common':
            return random.choice(self.common_passwords)
        elif password_type == 'pattern':
            return self.generate_pattern_password()
        else:
            return self.generate_random_password(random.randint(8, 16))
    
    def hash_password(self, password):
        """bcrypt를 사용하여 비밀번호 해시화"""
        # 비밀번호를 바이트로 인코딩
        password_bytes = password.encode('utf-8')
        
        # salt를 생성하고 해시화 (rounds=12, 적당한 보안 수준)
        salt = bcrypt.gensalt(rounds=12)
        hashed = bcrypt.hashpw(password_bytes, salt)
        
        # 문자열로 디코딩하여 반환
        return hashed.decode('utf-8')
    
    def generate_and_hash_password(self):
        """비밀번호 생성 후 해시화하여 (원본, 해시) 튜플 반환"""
        raw_password = self.generate_password()
        hashed_password = self.hash_password(raw_password)
        return raw_password, hashed_password
    
    def verify_password(self, password, hashed):
        """비밀번호 검증"""
        password_bytes = password.encode('utf-8')
        hashed_bytes = hashed.encode('utf-8')
        return bcrypt.checkpw(password_bytes, hashed_bytes)