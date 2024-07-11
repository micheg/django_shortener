### 1. Creazione di un Ambiente Virtuale

Prima di tutto, è una pratica consigliata utilizzare un ambiente virtuale per isolare le dipendenze del progetto. Ecco come farlo utilizzando `venv`:

#### Windows:

```bash
# Crea un nuovo ambiente virtuale nella cartella 'myproject_env'
python -m venv myproject_env

# Attiva l'ambiente virtuale
myproject_env\Scripts\activate
```

#### macOS/Linux:

```bash
# Crea un nuovo ambiente virtuale nella cartella 'myproject_env'
python3 -m venv myproject_env

# Attiva l'ambiente virtuale
source myproject_env/bin/activate
```

### 2. Installazione delle Dipendenze

Dopo aver attivato l'ambiente virtuale, puoi installare le dipendenze del progetto elencate nel file `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Creazione di un Nuovo Progetto Django

Creiamo un nuovo progetto Django chiamato `myproject`:

```bash
django-admin startproject myproject
cd myproject
```

### 4. Configurazione del Database

Modifica le impostazioni del database nel file `myproject/settings.py` per configurare il database che vuoi utilizzare (es. SQLite, PostgreSQL, MySQL).

```python
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### 5. Applicazione delle Migrazioni Iniziali

Applica le migrazioni iniziali per creare le tabelle del database:

```bash
python manage.py migrate
```

### 6. Creazione dell'Account Admin

Crea un superuser per accedere all'interfaccia di amministrazione di Django:

```bash
python manage.py createsuperuser
```

Segui le istruzioni per creare un nome utente, un indirizzo email e una password per l'account admin.

### 7. Avvio del Server di Sviluppo

Infine, avvia il server di sviluppo per verificare che tutto sia configurato correttamente:

```bash
python manage.py runserver
```

Ora puoi accedere al tuo progetto Django all'indirizzo `http://127.0.0.1:8000/` e all'interfaccia di amministrazione all'indirizzo `http://127.0.0.1:8000/admin/`.

