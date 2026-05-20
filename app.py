from inits.server_init import app
from database.index import lifespan
from analytics.middleware import AnalyticsMiddleware
from analytics.excluded_paths import EXCLUDE_PATHS
from router.app_router import page_router
from router.analytics_router import router as analytics_router
from router.auth_router import router as auth_router
from router.object_remover_router import router as object_remover_router



# ── Lifespan: DB connect / disconnect ────────────────────────────────────────
app.router.lifespan_context = lifespan

# ── Analytics middleware (records every non-excluded request) ─────────────────
app.add_middleware(AnalyticsMiddleware, exclude_paths=EXCLUDE_PATHS)

# ── Routers ───────────────────────────────────────────────────────────────────
app.include_router(page_router)              # / (UI)
app.include_router(analytics_router)         # /api/analytics
app.include_router(auth_router)              # /api/auth
app.include_router(object_remover_router) # /api/object-remover

