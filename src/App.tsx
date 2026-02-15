import { useState, useEffect } from 'react';
import { DotScreenShader } from '@/components/ui/dot-shader-background';
import './App.css';

interface Article {
  id: string;
  title: string;
  source: string;
  published_at: string;
  summary: string;
  url: string;
  image_url?: string;
}

function App() {
  const [articles, setArticles] = useState<Article[]>([]);
  const [savedIds, setSavedIds] = useState<string[]>(() => {
    const saved = localStorage.getItem('savedArticles');
    return saved ? JSON.parse(saved) : [];
  });
  const [view, setView] = useState('all');

  useEffect(() => {
    fetch('/articles.json')
      .then(res => res.json())
      .then(data => setArticles(data))
      .catch(err => console.error('Error loading articles:', err));
  }, []);

  const toggleSave = (id: string) => {
    const newSaved = savedIds.includes(id)
      ? savedIds.filter(i => i !== id)
      : [...savedIds, id];
    setSavedIds(newSaved);
    localStorage.setItem('savedArticles', JSON.stringify(newSaved));
  };

  const filteredArticles = view === 'saved'
    ? articles.filter(a => savedIds.includes(a.id))
    : articles;

  return (
    <div className="layout">
      {/* Dynamic Background */}
      <div className="fixed inset-0 -z-10 pointer-events-none opacity-50">
        <DotScreenShader />
      </div>

      {/* Sidebar Mockup */}
      <aside className="sidebar">
        <div className="logo-container">
          <img src="/logo.avif" alt="Logo" className="logo" />
          <div className="brand-name">
            <strong>B.L.A.S.T.</strong>
            <span>Dashboard</span>
          </div>
        </div>
        <nav className="side-nav">
          <button className={view === 'all' ? 'active' : ''} onClick={() => setView('all')}>
            <span className="icon">🏠</span> Feed
          </button>
          <button className={view === 'saved' ? 'active' : ''} onClick={() => setView('saved')}>
            <span className="icon">❤️</span> Saved
          </button>
        </nav>
      </aside>

      <main className="main-content">
        <header className="top-bar">
          <div className="search-mock">
            <span className="icon">🔍</span>
            <input type="text" placeholder="Search latest AI news..." readOnly />
          </div>
          <div className="user-profile">
            <div className="user-info">
              <strong>System Pilot</strong>
              <span>CEO Assistant</span>
            </div>
            <div className="avatar">SP</div>
          </div>
        </header>

        <section className="dashboard-stats">
          <div className="stat-card">
            <div className="stat-icon articles">📑</div>
            <div className="stat-info">
              <h3>{articles.length}</h3>
              <span>Total Articles</span>
            </div>
          </div>
          <div className="stat-card">
            <div className="stat-icon saved">❤️</div>
            <div className="stat-info">
              <h3>{articles.filter(a => savedIds.includes(a.id)).length}</h3>
              <span>Saved Articles</span>
            </div>
          </div>
          <div className="stat-card welcome">
            <div className="stat-info">
              <h3>Hey, Need help? 👋</h3>
              <span>Just ask me anything!</span>
            </div>
            <button className="ask-btn">→</button>
          </div>
        </section>

        <div className="bento-grid">
          {filteredArticles.length === 0 ? (
            <div className="empty-state bento-large">No articles found in the last 24h.</div>
          ) : (
            filteredArticles.map((article, index) => (
              <div
                key={article.id}
                className={`article-card ${index % 3 === 0 ? 'bento-large' : 'bento-small'}`}
              >
                <div className="card-header">
                  <span className="source-badge">{article.source}</span>
                  <button className={`save-btn ${savedIds.includes(article.id) ? 'saved' : ''}`} onClick={() => toggleSave(article.id)}>
                    {savedIds.includes(article.id) ? '❤️' : '🤍'}
                  </button>
                </div>

                {article.image_url && <img src={article.image_url} alt="" className="card-img" />}

                <div className="card-body">
                  <span className="date">{new Date(article.published_at).toLocaleDateString()}</span>
                  <h3>{article.title}</h3>
                  <p className="summary">{article.summary}</p>
                  <a href={article.url} target="_blank" rel="noopener noreferrer" className="read-more">
                    Read Feed →
                  </a>
                </div>
              </div>
            ))
          )}
        </div>
      </main>
    </div>
  );
}

export default App;
