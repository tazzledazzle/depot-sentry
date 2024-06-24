The warning message indicates that `urllib3` version 2.0 and above only supports OpenSSL 1.1.1 and newer versions, but your current environment uses LibreSSL 2.8.3, which is not supported.

Here are a few ways to resolve this issue:

### 1. **Upgrade OpenSSL**

If possible, upgrade OpenSSL to version 1.1.1 or higher. This is the most straightforward solution, but it might not be feasible depending on your system setup and dependencies.

### 2. **Use an Older Version of `urllib3`**

If upgrading OpenSSL is not an option, you can downgrade `urllib3` to a version that supports LibreSSL 2.8.3. For example, `urllib3` version 1.26.x should be compatible.

```bash
pip install urllib3==1.26.15
```

### 3. **Use a Different Python Environment**

Create a new virtual environment and ensure it uses the correct version of OpenSSL. This might involve using a different Python distribution that bundles a compatible OpenSSL version.

### Steps to Upgrade OpenSSL on macOS (if applicable)

If you're using macOS and have Homebrew installed, you can upgrade OpenSSL using the following steps:

1. **Install OpenSSL via Homebrew**:

   ```bash
   brew install openssl@1.1
   ```

2. **Link OpenSSL**:

   ```bash
   brew link openssl@1.1 --force
   ```

3. **Set Environment Variables**:

   Add the following lines to your shell configuration file (e.g., `~/.bash_profile`, `~/.zshrc`):

   ```bash
   export PATH="/usr/local/opt/openssl@1.1/bin:$PATH"
   export LDFLAGS="-L/usr/local/opt/openssl@1.1/lib"
   export CPPFLAGS="-I/usr/local/opt/openssl@1.1/include"
   export PKG_CONFIG_PATH="/usr/local/opt/openssl@1.1/lib/pkgconfig"
   ```

4. **Restart Your Shell**:

   ```bash
   source ~/.bash_profile
   ```

5. **Rebuild Your Virtual Environment**:

   ```bash
   rm -rf .venv
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

### Verify OpenSSL Version

After performing the steps above, you can verify the OpenSSL version being used by Python:

```python
import ssl
print(ssl.OPENSSL_VERSION)
```

This should output the version of OpenSSL that Python is using.

By following these steps, you should be able to resolve the `NotOpenSSLWarning` warning and ensure that your environment is compatible with `urllib3` version 2.0 and above. If you have any other questions or need further assistance, feel free to ask!