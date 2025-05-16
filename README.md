🎬 Movie & Actor Explorer - Compte Rendu Simple

🧠 Objectif
Créer une application en deux parties :

Backend (FastAPI + PostgreSQL)
→ Gérer les films et les acteurs, et générer un résumé avec un LLM (Groq via Langchain).

Frontend (Streamlit)
→ Afficher un film aléatoire avec ses acteurs, et demander un résumé généré automatiquement.

⚙️ Technos Utilisées

          FastAPI (backend)

         SQLAlchemy (modèles & relations Movies ↔ Actors)

         PostgreSQL (base de données)

        Pydantic (modèles de données)

        Langchain + Groq (LLM)

        Streamlit (frontend)

       requests, dotenv (intégration & config)

🗂️ Structure du Projet

     database.py → Connexion à PostgreSQL

     models.py → Modèles SQLAlchemy : Movies, Actors avec relation

     main_fastapi.py → API backend avec endpoints :

    POST /movies/ → Ajouter un film et ses acteurs

    GET /movies/random/ → Récupérer un film aléatoire avec ses acteurs

    POST /generate_summary/ → Générer un résumé avec LLM

    main_streamlit.py → Interface utilisateur avec deux boutons :

    “🎲 Show Random Movie”

     “🧠 Get Summary”

     .env → Clé API Groq

      requirements.txt → Toutes les dépendances

✅ Fonctionnalités Principales

Backend

    Gère les films + acteurs (relation 1-N)

    Récupère un film au hasard avec ses acteurs

    Génère un résumé grâce à Groq via Langchain

Frontend

    Affiche un film aléatoire

    Affiche les acteurs

    Bouton pour générer un résumé par LLM

❓ Réponses aux Questions

1. Pourquoi faut-il commit le film avant d’ajouter les acteurs ?
→ Pour que l’ID du film soit disponible et utilisable comme clé étrangère (movie_id) dans les enregistrements d’acteurs.

2. Lazy loading vs eager loading (joinedload) ?
→ Lazy loading charge les relations plus tard (au moment de l'accès), ce qui peut faire plusieurs requêtes.
→ Eager loading (comme joinedload) charge tout d’un coup avec une seule requête SQL plus efficace quand tu sais que tu vas utiliser les relations.

3. Comment formater la liste d’acteurs pour un prompt ?
→ Ex :

python
Copier le code
", ".join([actor.actor_name for actor in movie.actors])
Ce qui donne une chaîne simple comme :
"Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page"

🚀 Test Final

Lancer le backend

     uvicorn main_fastapi:app --reload
     
→ Ajouter les films via /docs (Swagger UI)

Lancer le frontend

         streamlit run main_streamlit.py
Tester :

Cliquer sur “Show Random Movie”

Puis “Get Summary”





![image](https://github.com/user-attachments/assets/a1ec3bfc-48d0-4cc4-9185-1f8ad0be843b)
